import { PUBLIC_API_URL } from '$env/static/public';
import { redirect, fail } from '@sveltejs/kit';

/** @type {import('./$types').Actions}*/
export const actions = {
    default: async ({ request, cookies }) => {
        const form = await request.formData();
        const email = form.get('email');
        const password = form.get('password');


        const data = new FormData();
        data.set('username', email);
        data.set('password', password);

        const response = await fetch(`${PUBLIC_API_URL}/auth-tokens`, {
            method: 'POST',
            body: data,
        });


        if (response.ok) {
            const { access_token } = await response.json();

            cookies.set('access_token', access_token, {
                path: '/not-existing-path',
                httpOnly: true,
                maxAge: 60 * 60 * 24 * 7, // 1 week
            });

            throw redirect(303, '/');
        }
        else if (response.status === 403) { 
            return fail(403, {email, password, wrongCredentials: true});
        }
    }
};

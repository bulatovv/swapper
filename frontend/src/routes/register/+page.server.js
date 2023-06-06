import { PUBLIC_API_URL, PUBLIC_FRONTEND_DOMAIN } from '$env/static/public';
import { redirect, fail } from '@sveltejs/kit';
import { dev } from '$app/environment';

/** @type {import('./$types').Actions}*/
export const actions = {
    default: async ({ request, cookies }) => {
        const form = await request.formData();
        const email = form.get('email');
        const password = form.get('password');

        const response = await fetch(`${PUBLIC_API_URL}/users`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ email, password, name: email }),
        });

        if (response.ok) {
            const data = new FormData();
            data.set('username', email);
            data.set('password', password);
            

            const response = await fetch(`${PUBLIC_API_URL}/auth-tokens`, {
                method: 'POST',
                body: data,
            });

			

			const accessToken = (await response.json())['access_token'];

            cookies.set('access_token', accessToken, {
                path: '/',
                sameSite: 'strict',
                domain: dev ? 'localhost' : PUBLIC_FRONTEND_DOMAIN,
                maxAge: 60 * 60 * 24 * 7, // 1 week
            });

            throw redirect(303, '/');
        }
        else if (response.status === 409) { 
            return fail(409, { email, emailExists: true });
        }
    }
};

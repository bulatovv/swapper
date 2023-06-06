import { PUBLIC_API_URL, PUBLIC_FRONTEND_DOMAIN } from '$env/static/public';
import { redirect, fail } from '@sveltejs/kit';

import { dev } from '$app/environment';
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
            const data = await response.json();

            const accessToken = data['access_token'];

            cookies.set('access_token', accessToken, {
                path: '/',
                sameSite: 'strict',
                domain: dev ? 'localhost' : PUBLIC_FRONTEND_DOMAIN,
                maxAge: 60 * 60 * 24 * 7, // 1 week
            });

            throw redirect(303, '/');
        }
        else if (response.status === 403) { 
            return fail(403, {email, password, wrongCredentials: true});
        }
    }
};

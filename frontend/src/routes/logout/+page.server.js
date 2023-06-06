import { PUBLIC_API_URL } from '$env/static/public';
import { redirect, error } from '@sveltejs/kit';


/** @type {import('./$types').Actions}*/
export const actions = {
	default: async ({ cookies }) => {
		if (cookies.get('access_token')) {
			const data = new FormData();
			const accessToken = cookies.get('access_token');
			data.set('access_token', accessToken);

			const response = await fetch(`${PUBLIC_API_URL}/auth-tokens`, {
				method: 'DELETE',
				body: data,
				headers: {
					'Authorization': `Bearer ${accessToken}`
				}
			});
			
			if (!response.ok) {
				throw error(response.status, await response.text());
			}

			cookies.delete('access_token');
		}

		throw redirect(303, '/');
	}
};

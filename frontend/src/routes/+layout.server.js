import { PUBLIC_API_URL } from '$env/static/public';


/** @type {import('./$types').LayoutServerLoad} */
export async function load({ cookies }) {

    const accessToken = cookies.get('access_token');   

    if (!accessToken) {
        return {};
    }

    const response = await fetch(`${PUBLIC_API_URL}/users/me`, {
		headers: {
			'Authorization': `Bearer ${accessToken}`,
		}
	});
    const user = await response.json();
	
	console.log(user);

    return { user };
}

import { PUBLIC_API_URL } from '$env/static/public';
import { redirect, fail } from '@sveltejs/kit';

/** type {import('./$types').Actions} */
export const actions = {
    default: async ({ request, cookies }) => {
        const form = await request.formData();
        
        const item = {
            'title': form.get('title'),
            'description': form.get('description'),
            'image_url': form.get('image_url'),
        };

        console.log('item', item);

        const userId = form.get('user_id');
            
        const response = await fetch(`${PUBLIC_API_URL}/items`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${cookies.get('token')}`,
            },
            body: JSON.stringify({
                item,
                'user_id': userId
            }),
        });

        if (response.ok) {
            throw redirect(303, '/');
        }
        else {
            const err = await response.json();
            console.log('err', err['detail'][0]);
            return fail(response.status, { message: response.statusText, error: true });
        }

    }
};

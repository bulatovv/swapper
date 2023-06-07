import { fileTypeFromBuffer } from 'file-type';
import { writeFile } from 'fs/promises';
import { Buffer } from 'buffer';
import { error } from '@sveltejs/kit';
import { PUBLIC_FRONTEND_URL } from '$env/static/public';

/** @type {import('./$types').RequestHandler} */
export async function POST({ request }) {
    const form = await request.formData();
    const file = form.get('image');

    if (!file) {
        return error(400, 'No file provided');
    }

    console.log('file', file);
    const filename = `${Date.now()}-${encodeURIComponent(file.name)}`;

    const buffer = await file.arrayBuffer();
    
    const fileType = await fileTypeFromBuffer(buffer);

    if (! fileType.mime.startsWith('image/')) {
        return error(400, 'File is not an image');
    }

    await writeFile(`./storage/images/${filename}`, Buffer.from(buffer));

    return new Response(JSON.stringify({ 'image_url': `${PUBLIC_FRONTEND_URL}/images/${filename}` }), { 
        headers: {
            'Content-Type': 'application/json',
        },
        status: 201
    });
}

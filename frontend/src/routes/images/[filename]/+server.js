import { fileTypeFromBuffer } from 'file-type';
import { readFile } from 'fs/promises';


/** @type {import('./$types').RequestHandler} */
export async function GET({ params }) {
    
    const filename = encodeURIComponent(params.filename);

    const buffer = await readFile(`./storage/images/${filename}`);

    const contentType = await fileTypeFromBuffer(buffer);

    return new Response(buffer, {
        headers: {
            'Content-Type': contentType.mime,
        }
    });
}

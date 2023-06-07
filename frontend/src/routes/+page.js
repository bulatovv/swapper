import { faker } from '@faker-js/faker';
import { PUBLIC_API_URL } from '$env/static/public';

export async function load({ parent, fetch }) {
    const { user } = await parent();

	let response = await fetch(`${PUBLIC_API_URL}/users`);
	const users = await response.json();

    const replies = [];
    const swaps = [];

	response = await fetch(`${PUBLIC_API_URL}/items`);
    const adverts = await response.json();
	

    for (let i = 0; i < 5; i++) {
        replies.push({
            id: faker.datatype.number(),
            user: users[Math.floor(Math.random() * users.length)].name,
            title: faker.commerce.productName(),
            description: faker.lorem.paragraphs(3),
            community: faker.address.street(),
            image: faker.image.abstract(640, 480, true),
        })
    }
    for (let i = 0; i < 3; i++) {
    swaps.push({
        id: faker.datatype.number(),
        user: users[Math.floor(Math.random() * users.length)].name,
        titleF: faker.commerce.productName(),
        titleS: faker.commerce.productName(),
        imageF: faker.image.abstract(640, 480, true),
        imageS: faker.image.abstract(640, 480, true),
        })
    }
    return { adverts, replies, swaps, user};
}

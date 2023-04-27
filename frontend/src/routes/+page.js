import { faker } from '@faker-js/faker';

export function load({ params }) {
    const adverts = [];
    const users = [];
    const replies = [];
    const swaps = [];
    for (let i = 0; i < 4; i++) {
        users.push({
            userid: faker.datatype.number(),
            name: faker.name.firstName(),
        })
    }
    for (let i = 0; i < 15; i++) {
        adverts.push({
            id: faker.datatype.number(),
            user: users[Math.floor(Math.random() * users.length)].name,
            title: faker.commerce.productName(),
            description: faker.lorem.paragraphs(3),
            community: faker.address.street(),
            image: faker.image.abstract(640, 480, true),
        })
    }
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
    return {
    adverts: adverts,
    replies: replies,
    swaps: swaps
    };
}

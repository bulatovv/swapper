import { faker } from '@faker-js/faker';

export function load({ params }) {
    const adverts = [];
    for (let i = 0; i < 50; i++) {
        adverts.push({
            id: faker.datatype.number(),
            title: faker.commerce.productName(),
            description: faker.lorem.paragraphs(3),
            community: faker.address.street(),
            image: faker.image.abstract(640, 480, true),
        })
    }
    return { adverts: adverts };
}

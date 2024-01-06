const assert = require('assert');
const axios = require('axios');

describe('Microservice Tests', () => {
    it('Deveria retornar Oi do JavaScript microservice!', async () => {
        const response = await axios.get('http://localhost:3000/oi');
        assert.strictEqual(response.status, 200);
        assert.strictEqual(response.data, 'Oi do JavaScript microservice!');
    });
});

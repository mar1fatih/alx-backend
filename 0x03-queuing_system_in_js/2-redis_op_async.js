import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

client.on('error', (err) => {
    console.log('Redis client not connected to the server: ' + err);
});

client.on('connect', () => {
    console.log('Redis client connected to the serve');
});

const pro_get = promisify(client.get).bind(client);
const pro_set = promisify(client.set).bind(client);

const setNewSchool = async (schoolName, value) => {
    try {
      const reply = await pro_set(schoolName, value);
      console.log(`Reply: ${reply}`);
    } catch (err) {
        console.log('ERROR: ' + err);
    }
};

const displaySchoolValue = async (schoolName) => {
    const rep = await pro_get(schoolName);
    console.log(rep);
};


const main = async () => {
    await displaySchoolValue('Holberton');
    await setNewSchool('HolbertonSanFrancisco', '100');
    await displaySchoolValue('HolbertonSanFrancisco');
};

main();

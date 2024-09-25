import redis from 'redis';

const client = redis.createClient();

client.on('error', (err) => {
    console.log('Redis client not connected to the server: ' + err);
});

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

const cities = {
    Portland: 50,
    Seattle: 80,
    'New York': 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2
};

for (let key in cities) {
    client.hset('HolbertonSchools', key, cities[key], redis.print);
}
client.hgetall('HolbertonSchools', (err, rep) => {
    if (err) {
        console.log(err);
    }
    console.log(rep);
});

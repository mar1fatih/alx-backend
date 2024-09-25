import kue from 'kue';

const queue = kue.createQueue();

const data = {
    phoneNumber: '0660660198',
    message: 'hello moto',
}
const job = queue.create('push_notification_code', data).save((err) => {
    if (!err) {
        console.log('Notification job created: ' + job.id);
    } else {
        console.log('Notification job failed');
    }
})

job.on('complete', (res) =>{
    console.log('Notification job completed');
});

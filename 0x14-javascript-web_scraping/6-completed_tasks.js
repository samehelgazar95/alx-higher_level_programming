#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, (err, res, body) => {
  err && console.log(err);

  const data = JSON.parse(body);
  const completedTasks = {};

  data.forEach((e) => {
    const completed = e.completed;
    const userId = e.userId;

    if (completed && !completedTasks[userId]) { completedTasks[userId] = 0; }
    if (completed) { completedTasks[userId]++; }
  });

  console.log(completedTasks);
});

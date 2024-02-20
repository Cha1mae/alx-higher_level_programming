#!/usr/bin/node
// This script will help us computes the number of tasks completed
// by user id
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
    return;
  }
  const tasks = JSON.parse(body);
  const completedTasks = {};

  tasks.forEach((task) => {
    if (task.completed) {
      if (completedTasks[task.userId]) {
        completedTasks[task.userId] += 1;
      } else {
        completedTasks[task.userId] = 1;
      }
    }
  });

  console.log(completedTasks);
});

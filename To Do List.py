#!/usr/bin/env python
# coding: utf-8

# In[40]:


# Define an empty list to store tasks

tasks = []


# In[41]:


# Function to add a task to the list

def add_task(task, completed=False):
    tasks.append({"task": task, "completed": completed})


# In[42]:


# Function to mark a task as completed

def complete_task(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True


# In[43]:


# Function to display the list of tasks

def display_tasks():
    for index, task in enumerate(tasks):
        status = "Done" if task["completed"] else "Not Done"
        print(f"{index + 1}. {task['task']} ({status})")


# In[44]:


# Function to get user input for a new task

def get_user_input():
    task = input("Enter a new task: ")
    completed = input("Is it done? (yes/no): ").lower() == "yes"
    return task, completed


# In[47]:


# Sample usage

while True:
    user_task, user_completed = get_user_input()
    add_task(user_task, user_completed)
    
    another_task = input("Do you want to add another task? (yes/no): ").lower()
    if another_task != "yes":
        break


# In[48]:


display_tasks()


# In[ ]:





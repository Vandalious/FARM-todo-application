import './App.css';
import React from 'react'
import Todo from './Todo'

export default function TodoList({ todos, doneTodo }) {
  return (
    <div className='TodoList'>
      {todos.map(todo => {
        return <Todo key={todo.title} todo={todo} doneTodo={doneTodo}/>
      })}
    </div>
  );
}

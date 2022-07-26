import './App.css';
import React from "react";
import Form from 'react-bootstrap/Form';

export default function Todo({ todo, doneTodo }) {

    function handleDoneTodo(e) {
        doneTodo(todo.title);
    }

    return (
        <div className='Todo'>
            <div className="title-priority">
                <Form.Label className="title fs-4"> {todo.title} </Form.Label>
                <Form.Label className="priority">Priority Level: {todo.priority}</Form.Label>
                <button className="done-button" onClick={handleDoneTodo}>
                    Done
                </button>
            </div>
            <div className='detail'> {todo.detail} </div>
        </div>
    );
}

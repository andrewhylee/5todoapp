import React from 'react'
// Import Components
import Todo from './Todo'

const ToDoList = ( {todos} ) => {
    console.log(todos)
    return(
        <div className="todo-container">
            <ul className="todo-list">
                {todos.map(todo => (
                    <Todo text={todo.text} id={todo.id} completed={todo.completed}/>
                ))}
            </ul>
        </div>
    )
}

export default ToDoList;
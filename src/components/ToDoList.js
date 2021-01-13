import React from 'react'
// Import Components
import Todo from './Todo'

const ToDoList = ({ todos, setTodos, filteredTodos }) => {
    console.log(todos)
    return (
        <div className="todo-container">
            <ul className="todo-list">
                {filteredTodos.map(todo => (
                    <Todo 
                        text={todo.text} 
                        key={todo.id} 
                        setTodos={setTodos} 
                        todos={todos}
                        todo={todo} />
                ))}
            </ul>
        </div>
    )
}

export default ToDoList;
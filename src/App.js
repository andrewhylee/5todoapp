import React, { useState, useEffect } from 'react';
import './App.css';
import Form from './components/Form';
import ToDoList from './components/ToDoList';

function App() {
  // State Stuff
  const [inputText, setInputText] = useState("");
  const [todos, setTodos] = useState([]);
  const [status, setStatus] = useState("all");
  const [filteredTodos, setFilteredTodos] = useState([]);

  // Run once when the app starts
  useEffect( () => {
    getLocalTodos()
  }, [] ) 
  
  // Use Effect
  useEffect( () => {
    filterHandler()
    saveLocalTodos()
  }, [ todos, status])

  // Functions
  const filterHandler = () => {
    switch(status){
      case 'completed':
        setFilteredTodos(todos.filter(todo => todo.completed === true) )
        break;
      case 'uncompleted':
        setFilteredTodos(todos.filter(todo => todo.completed !== true) )
        break;
      default:
        setFilteredTodos(todos);
        break;
    }
  }

  // Save to Local
  const saveLocalTodos = () => {
      localStorage.setItem('todos', JSON.stringify(todos))
    
  }

  // GetLocal 
  const getLocalTodos = () => {
    if(localStorage.getItem('todos') === null ){
      localStorage.setItem('todos', JSON.stringify([]))
    }else{
      let todoLocal = JSON.parse(localStorage.getItem('todos'))
      setTodos(todoLocal)
    }
  }



  return (
    <div className="App">
      <header>
        <h1>Drew's To Do List</h1>
      </header>
      <Form 
        inputText={inputText} 
        todos={todos}
        setTodos={setTodos} 
        setInputText={setInputText}
        setStatus={setStatus} />
      <ToDoList 
        todos={todos}         
        filteredTodos={filteredTodos} 
        setTodos={setTodos}/>
    </div>
  );
}

export default App;

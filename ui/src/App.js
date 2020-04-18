import React, { useState, useEffect } from 'react';
import styled from 'styled-components';
import io from "socket.io-client"
const socket = io('http://127.0.0.1:5000')

function handleSubmit() {
    console.log('hi')
}

function handleChange() {
    console.log('hi')
}

class App extends React.Component {

 componentDidMount () {
    this.setSocketListeners()
  }

   setSocketListeners () {
    socket.on('polarity_scores', (data) => {
      console.log(data)
    })
  }

  render() {
    return <div className="App">
      <header className="App-header">
        <Border>
            <h1>Please select a twitter topic you would like to follow!</h1>
            <Form onSubmit={handleSubmit}>
                <label>
                    Topic:
                    <input type="text"  onChange={handleChange} />
                </label>
                <input type="submit" value="Submit" />
            </Form>
        </Border>
      </header>
    </div>
  };
}

const Form = styled.form`
    margin-left: 100px;
    margin-right: 100px;
    margin-top: 100px;
    margin-bottom: 100px;
`

const Border = styled.div`
    border: 2px;
    border-style: solid;
    width: 800px;
    height: 600px;
    margin: auto;
`

export default App;
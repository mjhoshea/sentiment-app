import React, { useState } from "react";
import { Redirect, useHistory } from 'react-router-dom';

function Search (){
    const [input, setInput] = useState ("")
    const history = useHistory();

    function handleChange(e){
        setInput(e.target.value)
    }

    function handleSubmit(){
        history.push("/analyze");
    }

    return(
        <div className="search-area">
        <form onSubmit={handleSubmit}>
            <input 
            autoComplete="off"
            type="text" 
            name="search" 
            placeholder="Select a twitter topic you would like to follow..."
            onChange={handleChange}
            value={input}
            />
            <div>    
            <input 
            onClick={()=> {
            console.log(input)
            }}
            type="submit" 
            value="TRACK" />
            </div>
            </form>
    </div>
    )
}

export default Search;
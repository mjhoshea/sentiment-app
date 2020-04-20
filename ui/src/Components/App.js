import React from 'react';
import Nav from "./Nav";
import Footer from "./Footer";
import Features from "./Features";
import Contact from "./Contact";
import Home from "./Home";
import Analyze from "./Analyze";
import {
  BrowserRouter as Router,
  Route,
  Link,
  useRouteMatch,
  useParams
} from "react-router-dom";

// import io from "socket.io-client"
// const socket = io('http://127.0.0.1:5000')


function App() {

  // const setSocketListeners = () => {
  //   socket.on('polarity_scores', (data) => {
  //     console.log(data)
  //   })
  // };
  
  // const [listener, setListener] = useState(setSocketListeners)


  
  return (
    <Router>
    <div>
    <Nav />
      <Route exact path="/"><Home /></Route>
      <Route path="/features"><Features /></Route>
      <Route path="/contact"><Contact /></Route>
      <Route path="/analyze"><Analyze /></Route>
    <Footer />
    </div>
    </Router>
    )
  }

export default App;
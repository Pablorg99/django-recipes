import React from 'react';
import RecipeCard from './Components/RecipeCard'

class App extends React.Component {

  state = {
    recipes: []
  };

  componentDidMount() {
    fetch("http://127.0.0.1:8000/api/recipes")
    .then(results => results.json())
    .then(data => {
      this.setState({ recipes: data })
    })
    .catch(console.log)
  }

  render() {
    return (
      <div>
        <RecipeCard />
      </div>
    );
  }
}

export default App
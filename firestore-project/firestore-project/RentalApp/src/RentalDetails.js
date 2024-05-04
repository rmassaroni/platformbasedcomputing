import './App.css';
import { useState } from 'react';
import { firestore } from "./firebase";
import Reviews from './Reviews';
import { addDoc, collection } from "@firebase/firestore";

function RentalDetails({id,name, pic, description, size}) {
  //state variable to hold the review entered into the textarea
  //needs to be state variable because it updates every time the user enters a keyboard stroke
  const [review, setReview] = useState("Write review here");
  
  /* Save the review to Firestore */
  function handleSubmit(e) {
    //this function prevents any default behavior the browser may have to a particular event.
    e.preventDefault();
    const ref = collection(firestore, "reviews");
    let review_data = {
      id: id,
      content: review
    }
    addDoc(ref, review_data);
    setReview("");
    
}
  return (
    <div className="App">
      <div>
        <h2>
      {name}
      </h2>
      </div>
      <img style={{height: 350, width: 650}}
      src={pic}
      alt={name} />
        <h3>
      {description}
      </h3>     
      {size}   
      <br></br>
      <br></br>
      {/* This is a form.
          Forms handle events like when the user enters data into a text field or when
          the user clicks a button to submit the form among other events.
          When an event happens an event handler function handles the event.
          Here we have two event handler functions - handleSubmit that takes the event
          object as a parameter and saves the data entered into the text area field to firestore.
          The second is the arrow function that is called when a user enters text into the
          textarea field. The value property is what to display in the textarea. */}
      <form onSubmit={handleSubmit}>
        <textarea name="review" rows="4" cols="50"
           value={review} onChange={(event)=>setReview(event.target.value)}></textarea>
       <br></br>
        <button type = "submit">Review</button>
      </form>
      {/* The Reviews component is called with an id. 
          The Reviews component displays all of the reviews for a property with the given id. */}
      <Reviews id={id} />
    </div>    
  );
}

export default RentalDetails;

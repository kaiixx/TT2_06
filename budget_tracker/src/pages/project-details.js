import React, { useEffect, useState } from "react";

function ProjectDetailsPage() {

  const [expenses, setExpenses] = useState([
        {
            "id": 1,
            "project_id": 2,
            "category_id": 2,
            "name": "Server Maintenance",
            "description": "Server maintenance and upgrading work to incorporate BC plans",
            "amount": 30000,
            "created_at": "2021-11-04T16:00:00.000Z",
            "created_by": "Jacky",
            "updated_at": "2021-11-06T16:00:00.000Z",
            "updated_by": "Jacky"
        },
        {
            "id": 2,
            "project_id": 3,
            "category_id": 4,
            "name": "Consultant",
            "description": "Consultancy services for integration work",
            "amount": 10000,
            "created_at": "2021-11-06T16:00:00.000Z",
            "created_by": "Helen",
            "updated_at": "2021-11-07T16:00:00.000Z",
            "updated_by": "Helen"
        }
    ]);


    const handleUpdate = (value) => {
        console.log(value);
    }

    const handleDelete = (value) => {
        setExpenses((preExpenses) => {
            const tmp = preExpenses.filter((expense) => expense.id !== value);
            setExpenses([...tmp]);
        })
    }

  return (
    <div className="project-details">
        {
            !(expenses) ?
            null :
            expenses.map(expense => 
                <div id={expense.id}>
                    <h1>{expense.name}</h1>
                    <h3>{expense.description}</h3>
                    <p>{expense.amount}</p>
                    <button onClick={(event) => handleUpdate(expense.id)}>Update expense</button>
                    <button onClick={(event) => handleDelete(expense.id)}>Delete expense</button>
                </div>    
            )
        }
    </div>
  );
}

export default ProjectDetailsPage;

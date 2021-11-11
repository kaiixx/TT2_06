import React, { useEffect, useState } from "react";


function ProjectDetailsPage({userInfor}) {

  const [expenses, setExpenses] = useState([
        {
            id: 1,
            project_id: 2,
            category_id: 2,
            name: "Server Maintenance",
            description: "Server maintenance and upgrading work to incorporate BC plans",
            amount: 30000,
            created_at: "2021-11-04T16:00:00.000Z",
            created_by: "Jacky",
            updated_at: "2021-11-06T16:00:00.000Z",
            updated_by: "Jacky"
        },
        {
            id: 2,
            project_id: 3,
            category_id: 4,
            name: "Consultant",
            description: "Consultancy services for integration work",
            amount: 10000,
            created_at: "2021-11-06T16:00:00.000Z",
            created_by: "Helen",
            updated_at: "2021-11-07T16:00:00.000Z",
            updated_by: "Helen"
        }
    ]);

    const handleDelete = (value) => {
        setExpenses((preExpenses) => {
            const tmp = preExpenses.filter((expense) => expense.id !== value);
            setExpenses([...tmp]);
        })
    }

    const handleUpdate = (value) => {
        let name = prompt("enter the new name");
        let description = prompt("enter the new description");
        let amount = prompt("enter the new amount");

        console.log(userInfor);

        let exp = null;
        for(let i=0; i < expenses.length; i++) {
            if(expenses[i].id === value) exp = {...expenses[i]};
        }
        if(name.length !== 0) exp.name = name;
        if(description.length !== 0) exp.description = description;
        if(amount > 0) exp.amount = amount;
        exp.updated_at = (new Date()).toISOString();
        exp.updated_by = userInfor.name;
        
        console.log(exp);
        const tmp = expenses.map((expense) => {
            if(expense.id === value) return exp;
            return expense;
        });
        setExpenses([...tmp]);
    }

    console.log(userInfor);

  return (
    <div className="project-details">
        <button>Add expense</button>
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
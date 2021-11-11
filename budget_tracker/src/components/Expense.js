import Button from "react-bootstrap/Button";
const Expense = ({expense}) => {

    return(
        <div className = 'expense_wrap'>
        <div
            className = 'expense'
        >
        <h3>
            {expense.name}
            <Button style = {{backgroundColor: 'blue', border: "1px solid blue", marginLeft:"2%", marginRight:"-30%"}}  block size="lg" type="submit">
                Edit Expense
            </Button>  
            <Button style = {{backgroundColor: 'red', border: "1px solid red", marginLeft:"2%", marginRight:"0%"}}  block size="lg" type="submit">
                 Delete Expense
            </Button>  
        </h3>
        <p>{expense.description}</p>
        <p>Cost: {expense.amount}</p>
        </div>
        <p/>
        </div>
    )
}

export default Expense
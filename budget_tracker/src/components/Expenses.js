import Expense from "./Expense"

const Expenses = ({ expenses }) => {
    return(
        <>
            {expenses.map((expense) => (
                <Expense key  = {expense.id} expense ={expense}/>
            ))}
        </>
    )
}

export default Expenses
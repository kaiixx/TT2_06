

const Project = ({project}) => {
    return(
        <div
            className = 'project'
        >
        <h3>
            {project.name} ({project.description}){' '}
        </h3>    
        <p>Budget: {project.budget}</p>
        </div>
    )
}

export default Project
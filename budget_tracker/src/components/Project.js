

const Project = ({project}) => {
    return(
        <div
            className = 'project'
        >
        <h3>
            {project.name}{' '}
        </h3>    
        <p>{project.description}</p>
        </div>
    )
}

export default Project
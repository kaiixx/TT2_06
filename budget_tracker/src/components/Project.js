import {Link} from "react-router-dom";

const Project = ({project}) => {
    return(
        <div
            className = 'project'
        >
        <Link to="/project-details">
            <h3>
                {project.name} ({project.description}){' '}
            </h3>    
        </Link>
        <p>Budget: {project.budget}</p>
        </div>
    )
}

export default Project
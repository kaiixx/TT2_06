import Project from "./Project"
import { useState } from 'react';
import Projects from './Projects';

const Dashboard = () => {
    const[projects, setProjects] =  useState(
        [
            {
                "id": 1,
                "user_id": 4,
                "name": "RTF",
                "budget": 12000,
                "description": "Realtime Face Recogniton"
            },
            {
                "id": 2,
                "user_id": 1,
                "name": "SWT",
                "budget": 80000,
                "description": "Smart Watch Tracker"
            },
            {
                "id": 3,
                "user_id": 2,
                "name": "ULS",
                "budget": 11000,
                "description": "Upgrade Legacy System"
            }
          ]
    )
    
      return (
        <div>
          <h1> Projects </h1>
              <Projects projects = {projects}
              />
        </div>
      )
}

export default Dashboard;
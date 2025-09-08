import React from 'react';
import { Users, Award } from 'lucide-react';
import './Credits.css';

const Credits = () => {
  const teamMembers = [
    {
      id: 1,
      name: "Kamal Elsayed Elashry",
      studentId: "119"
    },
    {
      id: 2,
      name: "Mohammed Ahmed Ezz Eldin",
      studentId: "192"
    },
    {
      id: 3,
      name: "Youssef Hassan Abdelmoaty Hassan",
      studentId: "287"
    }
  ];

  return (
    <div className="credits-container">
      <div className="credits-card">
        <div className="credits-icon">
          <Users className="icon" />
        </div>
        <h2 className="credits-title">Project Credits</h2>
        <div className="project-info">
          <div className="project-badge">
            <Award className="badge-icon" />
            <span>Project 1 - Team A5</span>
          </div>
        </div>

        {/* Members grid uses CSS classes that render the card boxes */}
        <div className="members-grid">
          {teamMembers.map((member) => (
            <div key={member.id} className="member-card">
              <div className="member-icon">
                <Users className="icon" />
              </div>
              <div className="member-info">
                <h3 className="member-name">{member.name}</h3>
                <p className="member-id">ID: {member.studentId}</p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default Credits;

import React from 'react';
import { Users, Award, Code } from 'lucide-react';
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
        <div className="header">
          <Users className="icon" />
        </div>
        <h2 className="credits-title">Project Credits</h2>
        <div className="project-info">
          <div className="project-badge">
            <Award className="badge-icon" />
            <span>Project 1 - Team A5</span>
          </div>
        </div>

        <div className="team-list">
          {teamMembers.map((member) => (
            <div key={member.id} className="team-member">
              <div className="member-main">
                <div className="member-avatar">{member.name.charAt(0)}</div>
                <div className="member-details">
                  <h3 className="member-name">{member.name}</h3>
                  <p className="member-id">ID: {member.studentId}</p>
                </div>
              </div>
            </div>
          ))}
        </div>

        <div className="footer-note">
          <Code className="badge-icon" />
          <span>Special thanks to IEEE BUSB Vol. 2.0 Camp</span>
        </div>
      </div>
    </div>
  );
};

export default Credits;

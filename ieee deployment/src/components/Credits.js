import React from 'react';
import { Users, Award, Code } from 'lucide-react';
import './Credits.css';

const Credits = () => {
  const teamMembers = [
    {
      id: 1,
      name: "Youssef Hassan Abdelmoaty Hassan",
      studentId: "287"
    },
    {
      id: 2,
      name: "Kamal Elsayed Elashry",
      studentId: "119"
    },
    {
      id: 3,
      name: "Mohammed Abdelfatah Nabil Abdelfatah",
      studentId: "191"
    }
  ];

  return (
    <section className="credits-section">
      <div className="credits-container">
        <div className="credits-header">
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
        </div>

        <div className="team-members">
          <div className="members-grid">
            {teamMembers.map((member) => (
              <div key={member.id} className="member-card">
                <div className="member-icon">
                  <Code className="icon" />
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
    </section>
  );
};

export default Credits;

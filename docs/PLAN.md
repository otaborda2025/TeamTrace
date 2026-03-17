# Field Workforce Tracking SaaS – 120-Day Roadmap

## Project Overview
**Goal:** Build a full-stack SaaS for tracking employee locations on job sites, replacing Connecteam functionality, with mobile-friendly employee app and manager dashboard.

**Tech Stack:**
- Frontend: React + Tailwind CSS (PWA)
- Backend: Python + FastAPI
- Database: PostgreSQL
- Deployment: Render / Vercel / Supabase
- Authentication: JWT

---

## MVP Features

### Users & Roles
- **Employee**
  - Login/logout
  - Start/end shift (check-in/out)
  - Continuous GPS tracking (background)
  - View current shift status (on-site/off-site)
- **Manager**
  - Login/logout
  - Create/edit/delete employees
  - Create/edit/delete job sites
  - View employee map with real-time locations
  - See reports: time per job site, off-site alerts

### Backend API Endpoints
**Auth**
- `/api/auth/register` POST
- `/api/auth/login` POST
- `/api/auth/logout` POST

**Employees**
- `/api/employees` GET, POST
- `/api/employees/{id}` GET, PUT, DELETE

**Job Sites**
- `/api/job_sites` GET, POST
- `/api/job_sites/{id}` GET, PUT, DELETE

**Location Tracking**
- `/api/location_logs` POST
- `/api/location_logs` GET
- `/api/geofence_check` POST

**Sessions / Shifts**
- `/api/sessions/start` POST
- `/api/sessions/end` POST
- `/api/sessions/{employee_id}` GET

**Reports**
- `/api/reports/daily` GET
- `/api/reports/weekly` GET
- `/api/reports/export` GET (CSV/Excel)

### Frontend Pages / Components
**Employee App**
- LoginPage
- Dashboard
- CheckInButton / CheckOutButton
- LocationTracker
- ShiftHistory (optional)

**Manager Dashboard**
- LoginPage
- EmployeeList
- JobSiteList
- MapView
- EmployeeMarker
- ReportsPage
- ExportButton

**Shared Components**
- Header, Footer, AlertPopup

---

## 120-Day Week-by-Week Plan

### Week 1 – Phase 0: Setup & Planning
- Install Python, Node.js, VS Code
- Install Git; create GitHub repo
- Create folder structure (`frontend`, `backend`, `database`, `docs`)
- Sketch wireframes (employee app & manager dashboard)
- List MVP features
- Optional: draft README

### Week 2 – Phase 1: Backend Setup
- Initialize FastAPI project
- Install PostgreSQL
- Define database tables: employees, job_sites, location_logs, alerts, sessions
- Implement JWT authentication
- Test auth endpoints

### Week 3 – Phase 1: Backend CRUD APIs
- CRUD APIs for employees & job sites
- Validation with Pydantic
- Test with Postman
- Commit & document

### Week 4 – Phase 2: Location Logging & Geofencing
- Create API for location logging
- Implement geofencing logic (inside/outside job site)
- Store status in DB
- Test with sample data

### Week 5 – Phase 2: Sessions & Reports
- Check-in / Check-out API
- Track session start/end times
- Generate basic report: time per job site
- Test with sample data

### Week 6 – Phase 3: React Frontend Setup
- Create React project (CRA or Vite)
- Install Tailwind CSS
- Login page & form validation
- Basic navigation

### Week 7 – Phase 3: Employee App MVP
- Implement check-in/check-out UI
- Capture GPS coordinates from mobile
- Send location to backend
- Show shift status (on-site/off-site)
- Test with sample employees

### Week 8 – Phase 3: Mobile Testing & Polishing
- Mobile layout fixes & responsiveness
- Debug API/frontend issues
- Minor UI enhancements

### Week 9 – Phase 4: Manager Dashboard Setup
- React dashboard setup
- Map integration (Leaflet / Google Maps)
- Display job sites & employee locations

### Week 10 – Phase 4: Dashboard Features
- Employee status indicators
- Job site filtering
- Charts: time per job site
- UI polish

### Week 11 – Phase 4: Dashboard Polishing
- Mobile responsiveness
- Test map performance
- Debug syncing
- Commit & push

### Week 12 – Phase 5: Reports
- Backend endpoints: daily/weekly reports
- Export CSV/Excel
- Frontend charts
- Test reports with sample data

### Week 13 – Phase 5: Analytics Enhancements
- Add summary dashboard
- Visual indicators for alerts
- Test charts & exports
- Documentation updates

### Week 14–16 – Phase 6: Continuous Tracking & Alerts
- Continuous GPS tracking in employee app
- Real-time updates in manager dashboard
- Alerts for employees outside job site
- Session management

### Week 17–18 – Phase 7: Production Setup
- Dockerize frontend & backend
- Deploy backend (Render/AWS/Heroku)
- Deploy frontend (Vercel/Netlify)
- Connect cloud PostgreSQL
- Configure environment variables & SSL

### Week 19–20 – Phase 8: Polish & Portfolio
- UI polish & final tweaks
- Add screenshots, demo video
- Write detailed README with architecture & features
- Push final code & sample datasets

---

## Notes / Tips
- Track progress in Trello/Notion or GitHub Projects
- Commit code every session
- Optional stretch goals after MVP:  
  - Real-time alerts via email/Slack  
  - Multi-company support  
  - Advanced analytics  

---

**Status:** Ready to start coding tomorrow!
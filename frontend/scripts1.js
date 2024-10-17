document.getElementById("getStartedBtn").addEventListener("click", function() {
    alert("Welcome to the Job Portal for Persons with Disabilities!");
});

// Dynamic job listings (example)
const jobs = [
    {
        title: "Front-end Developer",
        company: "Accessible Tech Solutions",
        location: "Remote",
        accessibility: "Remote work, Screen reader support"
    },
    {
        title: "HR Specialist",
        company: "Diversity Hiring Group",
        location: "London, UK",
        accessibility: "Wheelchair accessible office, sign language support"
    }
];

const jobListingsContainer = document.querySelector('.job-listings');

jobs.forEach(job => {
    const jobItem = document.createElement('div');
    jobItem.classList.add('job-item');
    
    jobItem.innerHTML = `
        <h3>${job.title}</h3>
        <p><strong>Company:</strong> ${job.company}</p>
        <p><strong>Location:</strong> ${job.location}</p>
        <p><strong>Accessibility Features:</strong> ${job.accessibility}</p>
        <button class="apply-btn">Apply Now</button>
    `;
    
    jobListingsContainer.appendChild(jobItem);
});

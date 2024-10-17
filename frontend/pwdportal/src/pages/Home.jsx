import React, { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { MetaData } from '../components/MetaData'
import { useSelector, useDispatch } from 'react-redux';
import { JobCard } from '../components/JobCard';
import { getAllJobs } from '../actions/JobActions';
import Testimonials from '../components/Testimonials/Testimonials.jsx';



export const Home = () => {

    const [num, setNum] = useState(2);
    const dispatch = useDispatch()
    const { loading, allJobs } = useSelector(state => state.job)
    const [jobs, setJobs] = useState([])


    // Update the data to reflect accessibility aids
    const data = [
        {
            link: "/images/Accessibility/Mobility-aids",
            feature: "Sign Language Interpreters"
        },
        {
            link: "/images/Accessibility/visual-aid.jpg",
            feature: "Visual Aids for Low Vision"
        },
        {
            link: "/images/Accessibility/mobility-aid.jpg",
            feature: "Mobility Aids"
        },
        {
            link: "/images/Accessibility/hearing-aid.jpg",
            feature: "Hearing Aids"
        },
        {
            link: "/images/Accessibility/closed-captioning.jpg",
            feature: "Closed Captioning"
        },
        {
            link: "/images/Accessibility/accessible-tech.jpg",
            feature: "Accessible Technology"
        }
    ]


    useEffect(() => {
        dispatch(getAllJobs())

    }, [])



    const convertDateFormat = (inputDate) => {
        const parts = inputDate.split('-');
        if (parts.length !== 3) {
            return "Invalid date format";
        }

        const day = parts[2];
        const month = parts[1];
        const year = parts[0];

        return `${day}-${month}-${year}`;
    }

    return (


        <>
            <MetaData title="AjiraBora" />
            <div className='min-h-screen md:px-20 px-3  pt-14 flex   text-white bg-gray-950'>
                <div className='  w-full  flex  pt-28 flex-col justify-start  items-center gap-4'>

                    <div className='flex md:flex-row flex-col items-center justify-center md:gap-10 gap-1'>
                        <div className='md:text-8xl text-6xl titleT'>AJIRABORA</div>
                        <div className=' flex justify-center items-center pt-1'>
                            <Link to="/jobs" className='font-semibold md:text-2xl text-lg blueCol  md:py-3 py-2 px-6 md:px-10 '>Browse Jobs</Link>
                        </div>
                    </div>
                    <div>
                        <p className='md:text-xl text-sm'>Empowering <span className='text-yellow-500'>Ability</span>, Connecting Opportunity.</p>
                        
                    </div>

                    <div className='pt-[8rem] md:px-[1rem] px-[0rem] w-full'>
    <div className='titleT pb-6 text-2xl'>
        <p className='titleT'>Current Listings</p>
    </div>
    <div>
        {loading ? (
            <div className='w-full  flex justify-center items-center'>
                <span className="loader1"></span> 
            </div>
        ) : (
            <div>
                <div className='flex md:flex-row flex-col gap-3'>
                    {allJobs && allJobs.length >= 4 ? (
                        <>
                            <Link to={`/details/${allJobs[3]._id}`} className='flex gap-2 shadow-sm shadow-gray-800 border border-gray-700 md:w-[26rem] w-[21rem] p-2 flex-col hover:border-rose-500 transition duration-300 hover:scale-[1.02] hover:bg-slate-950'>
                                <div className='flex gap-3'>
                                    <div className='w-[5rem] flex justify-center items-center'>
                                        <img src={allJobs[3].companyLogo.url} alt={allJobs[3].title} className='w-[4rem]' />
                                    </div>
                                    <div>
                                        <p className='text-xl'>{allJobs[3].title}</p>
                                        <p className='text-lg'>{allJobs[3].companyName}</p>
                                        <p className='text-sm'>{allJobs[3].description.slice(0, 30) + "..."}</p>
                                    </div>
                                </div>
                                <div className='flex text-sm gap-8'>
                                    <span>{convertDateFormat(allJobs[3].createdAt.slice(0,10))}</span>
                                    <span>{allJobs[3].employmentType}</span>
                                    <span>
                                        {allJobs[3].location === "Remote"
                                            ? "Remote"
                                            : allJobs[3].location === "Hybrid"
                                            ? "Hybrid (Remote & In-person)"
                                            : "In-person"}
                                    </span>
                                </div>
                            </Link>
                            {/* Add other job listings similarly */}
                        </>
                    ) : null}
                </div>
            </div>
        )}
    </div>
</div>

<div className='pt-20 flex flex-col gap-4 md:px-[1rem] px-[1rem] '>
    <div className='text-2xl titleT'>
        Accessibility Features on our Site
    </div>

    {/* Buttons for Employers and Job Seekers */}
    <div className='flex gap-6 mt-4'>
        <Link to="/employers">
            <button className='bg-blue-500 hover:bg-blue-600 text-white py-2 px-4 rounded-lg shadow-md transition duration-300'>
                Employers
            </button>
        </Link>
        <Link to="/jobseekers">
            <button className='bg-green-500 hover:bg-green-600 text-white py-2 px-4 rounded-lg shadow-md transition duration-300'>
                Job Seekers
            </button>
        </Link>
    </div>

    {/* Displaying Accessibility Features */}
    <div className="flex flex-wrap gap-3 mt-6">
        {
            data.map((e, i) => (
                <div key={i} className="flex flex-col items-center">
                    <img src={e.link} className='w-[6rem]' alt={e.feature} title={e.feature} />
                    <p className="text-center text-lg mt-2">{e.feature}</p>
                </div>
            ))
        }
    </div>
</div>


                    <Testimonials />
                    
                    <div className="pt-[7rem] pb-[10rem] md:px-[14rem] px-[1rem]   text-center">
                        <p>Unleash Your Potential with AjiraBora: Where Inclusive Opportunities Empower Your Career, Opening Doors to a Future Without Limits!</p>
                    </div>
                </div>
            </div>
        </>
    )
}

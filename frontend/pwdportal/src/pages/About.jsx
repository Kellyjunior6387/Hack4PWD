import React from 'react'
import { MetaData } from '../components/MetaData'


export const About = () => {
  return (
    <>
      <MetaData title="About" />
      <div className="bg-gray-900 min-h-screen pt-14 md:px-20 px-3 text-white">
  <div className="grid md:grid-cols-3 gap-5 md:px-0 px-2 md:pt-8 pt-4 pb-20">
    <div className="bg-gray-800 p-5 rounded-lg shadow-lg">
      <p className="text-2xl pb-3 text-center text-yellow-500">About Us</p>
      <p className="text-md">
      At AjiraBora, we are dedicated to empowering persons with disabilities by
              connecting them with meaningful employment opportunities.<br/><br/>Our mission is
              to create an inclusive job portal that bridges the gap between talented
              individuals with disabilities and employers committed to accessibility.
              Whether you are seeking your first job or looking to advance your career,
              JobLink is here to support you every step of the way.
      </p>
    </div>
    <div className="bg-gray-800 p-5 rounded-lg shadow-lg">
      <p className="text-2xl text-yellow-500 text-center">What Sets Us Apart</p>
      <p className="text-md"> <br/>
          We embrace individuality. Our platform is designed to meet the diverse
          needs of users, whether you navigate using screen readers, require mobility
          assistance, or depend on visual or auditory aids. We prioritize inclusivity,
          ensuring a seamless experience for everyone.<br/><br/> We go beyond just customer service. Our team is committed to your growth,
          offering hands-on assistance, from building an optimized profile to providing
          expert guidance for job interviews. Your success drives everything we do.
      </p>
    </div>
    <div className="bg-gray-800 p-5 rounded-lg shadow-lg">
      <p className="text-2xl text-yellow-500">Join us</p>
      <p className="pt-3">
        {" "}When you register with AjiraBora, you're not merely joining a job portal –
        you are stepping into a vibrant community dedicated to empowering individuals
        with disabilities.
      </p>
      <p className="pt-4">
        Thank you for choosing AjiraBora as your ally in navigating the job market.
        Together, we will unlock a multitude of opportunities and strive for
        excellence in every step of your career journey!
      </p>
    </div>
  </div>
</div>
    </>
  )
}

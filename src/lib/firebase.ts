// Import the functions you need from the SDKs you need
import { initializeApp } from 'firebase/app';
import { getAnalytics } from 'firebase/analytics';
import { getFirestore } from 'firebase/firestore';

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
	apiKey: 'AIzaSyAoQk8tUa7V5QGV6dG2wnT3By6mTOXl1wI',
	authDomain: 'redditrecs-tech.firebaseapp.com',
	projectId: 'redditrecs-tech',
	storageBucket: 'redditrecs-tech.appspot.com',
	messagingSenderId: '910608717493',
	appId: '1:910608717493:web:aefc117bb126e4727e90fc',
	measurementId: 'G-44EG974BCL'
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
const db = getFirestore(app);

export { db, analytics };

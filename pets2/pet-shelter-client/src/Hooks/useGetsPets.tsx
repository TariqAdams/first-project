import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
type DisplayPet = {
    petId: string;
    name: string;
    species: string;
    age: string;
    dateEntered: string;
    image: string;
};
export default function useGetPets() {
    const [pets, setPets] = useState<DisplayPet[]>([]);
    const navigate = useNavigate();
    useEffect(() => {
        async function getPets() {
            try {
                // TODO: Replace with your real backend fetch
                const dummyPets: DisplayPet[] = [
                    {
                        petId: '1',
                        name: 'Max',
                        species: 'Dog',
                        age: '3',
                        dateEntered: '2025-06-01',
                        image: 'https://via.placeholder.com/150',
                    },
                    {
                        petId: '2',
                        name: 'Whiskers',
                        species: 'Cat',
                        age: '2',
                        dateEntered: '2025-06-03',
                        image: 'https://via.placeholder.com/150',
                    },
                ];
                setPets(dummyPets);
            } catch (error) {
                console.error('Failed to fetch pets', error);
                navigate('/error', { state: { message: 'Failed to fetch pets' } });
            }
        }
        getPets();
    }, [navigate]);
    return pets;
}
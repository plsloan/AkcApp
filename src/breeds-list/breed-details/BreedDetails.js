import { Rate } from 'antd';
import Text from 'antd/lib/typography/Text';
import React, { useEffect, useState } from 'react';
import { withRouter } from 'react-router-dom';
import { breedData } from 'utils';

import './BreedDetails.css';

const BreedDetailsC = (props) => {
  let { id } = props.match.params;
  id = Number(id);

  const [breedDetails, setBreedDetails] = useState({ breed_name: '--', attributes: {}, traits: {}});
  const [temperament, setTemperament] = useState([]);
  const [breedPopularity, setBreedPopularity] = useState(-1);
  const [height, setHeight] = useState([]);
  const [weight, setWeight] = useState([]);
  const [lifeExpectancy, setLifeExpectancy] = useState([]);
  const [akcGroup, setAkcGroup] = useState('--');
  
  const defaultTraitObj = { description: '--', rating: 0};
  const [energyLevel, setEnergyLevel] = useState(defaultTraitObj);
  const [groomingFrequency, setGroomingFrequency] = useState(defaultTraitObj);
  const [shedding, setShedding] = useState(defaultTraitObj);
  const [demeanor, setDemeanor] = useState(defaultTraitObj);
  const [trainability, setTrainability] = useState(defaultTraitObj);

  useEffect(() => {
    if (id !== undefined) {
      setBreedDetails(breedData[id]);

      const attributes = breedDetails['attributes'] || {};
      setTemperament(attributes['temperament'] || []);
      setBreedPopularity(attributes['breed_popularity'] || '--');
      setHeight(attributes['height'] || []);
      setWeight(attributes['weight'] || []);
      setLifeExpectancy(attributes['life_expectancy'] || []);
      setAkcGroup(attributes['group'] || '--');
      
      const traits = breedDetails['traits'] || {};
      setEnergyLevel(traits['energy_level'] || 0);
      setGroomingFrequency(traits['grooming_frequency'] || 0);
      setShedding(traits['shedding'] || 0);
      setDemeanor(traits['temperament_demeanor'] || 0);
      setTrainability(traits['trainability'] || 0);
    }
  }, [id, breedDetails]);
  
  return (
    <>
      <h1>{breedDetails.breed_name}</h1>

      <div className='detailsContainer'>
        <div className='detailsColumn'>
          <h2>Attributes</h2>

          <div className='attributesRow'>
            <Text><b>Temperament: </b>{temperament.join(', ')}</Text>
          </div>

          <div className='attributesRow'>
            <Text><b>Breed Popularity:  </b>{breedPopularity}</Text>
          </div>

          <div className='attributesRow'>
            <Text><b>Height:  </b>{height.join('-')} inches</Text>
          </div>

          <div className='attributesRow'>
            <Text><b>Weight:  </b>{weight.join('-')} lbs</Text>
          </div>

          <div className='attributesRow'>
            <Text><b>Life Expectancy:  </b>{lifeExpectancy.join('-')} years</Text>
          </div>

          <div className='attributesRow'>
            <Text><b>AKC Group:  </b>{akcGroup}</Text>
          </div>
        </div>
        
        <div className='detailsColumn'>
          <h2>Traits</h2>  
          
          <div className='traitsRow'>
            <Text><b>Energy Level: </b>{energyLevel['description']}</Text>
            <br />
            <Rate disabled value={energyLevel['rating']} />
          </div>
          
          <br />
          
          <div className='traitsRow'>
            <Text><b>Grooming Frequency: </b>{groomingFrequency['description']}</Text>
            <br />
            <Rate disabled value={groomingFrequency['rating']} />
          </div>
          
          <br />
          
          <div className='traitsRow'>
            <Text><b>Shedding: </b>{shedding['description']}</Text>
            <br />
            <Rate disabled value={shedding['rating']} />
          </div>
          
          <br />
          
          <div className='traitsRow'>
            <Text><b>Temperament/Demeanor: </b>{demeanor['description']}</Text>
            <br />
            <Rate disabled value={demeanor['rating']} />
          </div>
          
          <br />
          
          <div className='traitsRow'>
            <Text><b>Trainability: </b>{trainability['description']}</Text>
            <br />
            <Rate disabled value={trainability['rating']} />
          </div>
        </div>
      </div>
    </>
  );
}

export const BreedDetails = withRouter(BreedDetailsC)

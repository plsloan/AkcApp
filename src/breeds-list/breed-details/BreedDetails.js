import { Rate } from 'antd';
import Text from 'antd/lib/typography/Text';
import React, { useEffect, useState } from 'react';
import { withRouter } from 'react-router-dom';
import { apiFetch } from 'utils';

import './BreedDetails.css'

const defaultBreedData = { 'result': 'not set' };

const BreedDetailsC = (props) => {
  const { id } = props.match.params;
  const [breedData, setBreedData] = useState(defaultBreedData);
  
  useEffect(() => {
    if (breedData === defaultBreedData) {
      apiFetch(`/api/breed/${id}`).then(data => {
        setBreedData(data)
      })
    }
  }, [breedData, id]);

  const getValueFromPath = (obj, path) => {
    if (obj) {
      let value = obj;
      path.forEach(p => {
        console.log('next', value[p]);
        value = value[p];
      });
      return value;
    }

    return '';
  }
  
  const attributes = breedData['attributes']
  const temperament = getValueFromPath(attributes, ['temperament']);
  const breedPopularity = getValueFromPath(attributes, ['breed_popularity']);
  const height = getValueFromPath(attributes, ['height']);
  const weight = getValueFromPath(attributes, ['weight']);
  const lifeExpectancy = getValueFromPath(attributes, ['life_expectancy']);
  const akcGroup = getValueFromPath(attributes, ['group']);
  
  const traits = breedData['traits']
  
  return (
    <>
      <h1>{breedData.breed_name}</h1>

      <div className='detailsContainer'>
        <div className='detailsColumn'>
          <h2>Attributes</h2>

          <div className='attributesRow'>
            <Text><b>Temperament: </b>{temperament ? temperament.join(', ') : '--'}</Text>
          </div>

          <div className='attributesRow'>
            <Text><b>Breed Popularity:  </b>{breedPopularity || '--'}</Text>
          </div>

          <div className='attributesRow'>
            <Text><b>Height:  </b>{height ? height.join('-') : '--'} inches</Text>
          </div>

          <div className='attributesRow'>
            <Text><b>Weight:  </b>{weight ? weight.join('-') : '--'} lbs</Text>
          </div>

          <div className='attributesRow'>
            <Text><b>Life Expectancy:  </b>{lifeExpectancy ? lifeExpectancy.join('-') : '--'} years</Text>
          </div>

          <div className='attributesRow'>
            <Text><b>AKC Group:  </b>{akcGroup || '--'}</Text>
          </div>
        </div>
        
        <div className='detailsColumn'>
          <h2>Traits</h2>  
          
          <div className='traitsRow'>
            <Text><b>Energy Level: </b>{getValueFromPath(traits, ['energy_level', 'description'])}</Text>
            <br />
            <Rate disabled value={getValueFromPath(traits, ['energy_level', 'rating'])} />
          </div>
          
          <br />
          
          <div className='traitsRow'>
            <Text><b>Grooming Frequency: </b>{getValueFromPath(traits, ['grooming_frequency', 'description'])}</Text>
            <br />
            <Rate disabled value={getValueFromPath(traits, ['grooming_frequency', 'rating'])} />
          </div>
          
          <br />
          
          <div className='traitsRow'>
            <Text><b>Shedding: </b>{getValueFromPath(traits, ['shedding', 'description'])}</Text>
            <br />
            <Rate disabled value={getValueFromPath(traits, ['shedding', 'rating'])} />
          </div>
          
          <br />
          
          <div className='traitsRow'>
            <Text><b>Temperament/Demeanor: </b>{getValueFromPath(traits, ['temperament_demeanor', 'description'])}</Text>
            <br />
            <Rate disabled value={getValueFromPath(traits, ['temperament_demeanor', 'rating'])} />
          </div>
          
          <br />
          
          <div className='traitsRow'>
            <Text><b>Trainability: </b>{getValueFromPath(traits, ['trainability', 'description'])}</Text>
            <br />
            <Rate disabled value={getValueFromPath(traits, ['trainability', 'rating'])} />
          </div>
        </div>
      </div>
    </>
  );
}

export const BreedDetails = withRouter(BreedDetailsC)

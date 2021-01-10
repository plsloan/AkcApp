import { Collapse, Rate, Select } from 'antd';
import Text from 'antd/lib/typography/Text';
import React, { useState } from 'react';
import { withRouter } from 'react-router-dom';
import { breedData } from 'utils';

const BreedSearchC = (props) => {
  const { history } = props;
  const { Panel } = Collapse;
  const { Option } = Select;

  const [collapseActiveKey, setCollapseActiveKey] = useState(-1);
  const [filterGroom, setFilterGroom] = useState(5);
  const [filterShed, setFilterShed] = useState(5);
  const [filterEnergy, setFilterEnergy] = useState(5);
  const [filterTrain, setFilterTrain] = useState(0);
  const [filterTemper, setFilterTemper] = useState(0);

  const getTraitLabel = key => {
    switch (key) {
      case 'grooming_frequency':
        return 'Grooming Frequency';
      case 'shedding':
        return 'Shedding';
      case 'energy_level':
        return 'Energy Level';
      case 'trainability':
        return 'Trainability';
      case 'temperament_demeanor':
        return 'Temperament/Demeanor';
      default:
        return '';
    }
  }

  const getTraitRating = key => {
    switch (key) {
      case 'grooming_frequency':
        return filterGroom;
      case 'shedding':
        return filterShed;
      case 'energy_level':
        return filterEnergy;
      case 'trainability':
        return filterTrain;
      case 'temperament_demeanor':
        return filterTemper;
      default:
        return 0;
    }
  }

  const onChangeCollapseActiveKey = key => {
    if (key === collapseActiveKey) {
      setCollapseActiveKey(-1);
    } else {
      setCollapseActiveKey(key);
    }
  }

  const onChangeTraitFilter = key => value => {
    switch (key) {
      case 'grooming_frequency':
        setFilterGroom(value);
        break;
      case 'shedding':
        setFilterShed(value);
        break;
      case 'energy_level':
        setFilterEnergy(value);
        break;
      case 'trainability':
        setFilterTrain(value);
        break;
      case 'temperament_demeanor':
        setFilterTemper(value);
        break;
      default:
        break;
    }
  }

  const getTraitRatingFilters = () => {
    return Object.keys(breedData[0]['traits']).map(key => (
      <>
        <div>
          <Text>{getTraitLabel(key)}</Text>
          <br />
          <Rate onChange={onChangeTraitFilter(key)} value={getTraitRating(key)} />
        </div>
        <br />
      </>
    ));
  }

  const getSelectOptions = () => {
    const filteredBreedData = breedData.filter(obj => {
      const traits = obj['traits'];
      if (
        traits && 
        traits['grooming_frequency'] && (traits['grooming_frequency']['rating'] || 0) <= filterGroom && 
        traits['shedding'] && (traits['shedding']['rating'] || 0) <= filterShed && 
        traits['energy_level'] && (traits['energy_level']['rating'] || 0) <= filterEnergy && 
        traits['trainability'] && (traits['trainability']['rating'] || 0) >= filterTrain && 
        traits['temperament_demeanor'] && (traits['temperament_demeanor']['rating'] || 0) >= filterTemper
      ) {
        return true;
      }

      return false;
    });
    
    return filteredBreedData.map(obj => <Option key={obj['_id']} value={obj['breed_name']}>{obj['breed_name']}</Option>);
  }

  const onSelectBreedName = (_value, option) => { history.push(`/breeds/${option['key']}`) }

  return (
    <>
      <h1>Breed Search</h1>

      <Text><b>Breed Search:</b></Text><br />
      <Select onSelect={onSelectBreedName} showSearch style={{ width: '150px' }}>
          {getSelectOptions()}
      </Select>
      
      <br /><br />
      
      <Collapse activeKey={collapseActiveKey} onChange={onChangeCollapseActiveKey} >
        <Panel key={0} header="Minimum Breed Search Trait Rating Filters">
          {getTraitRatingFilters()}
        </Panel>
      </Collapse>
    </>
  );
}

export const BreedSearch = withRouter(BreedSearchC)

import { Table } from 'antd';
import React, { useEffect, useState } from 'react';
import { withRouter } from 'react-router-dom';
import { apiFetch } from 'utils';

const defaultBreedData = ['not set'];

const BreedsListC = (props) => {
  const { history } = props;
  const [breedData, setBreedData] = useState(defaultBreedData);
  
  useEffect(() => {
    if (breedData === defaultBreedData) {
      apiFetch('/api/breed-table').then(data => {
        setBreedData(data)
      })
    }
  }, [breedData]);

  const getStringOrRange = value => {
    if (typeof value === 'string') {
      return value;
    } else if (Array.isArray(value)) {
      return value.join('-');
    } else {
      return ''
    }
  };

  const tableColumns = [
    {
      title: 'Breed Name',
      dataIndex: 'breed_name',
      key: 'breed_name',
      sorter: (a, b) => a.breed_name.localeCompare(b.breed_name)
    },
    {
      title: 'Breed Popularity',
      dataIndex: 'breed_popularity',
      key: 'breed_popularity',
      filters: [
        { text: '1-50', value: '1-50' },
        { text: '51-100', value: '51-100' },
        { text: '101-150', value: '101-150' },
        { text: '151-200', value: '151-200' }
      ],
      onFilter: (value, record) => {
        if (value) {
          const valueSplit = value.split('-')
          const valueArray = valueSplit.map(w => Number(w))
          
          if (record.breed_popularity) {
            return record.breed_popularity >= valueArray[0] && record.breed_popularity <= valueArray[1];
          }

          return false;
        }

        return false;
      },
      sorter: (a, b) => (a.breed_popularity || 0) - (b.breed_popularity || 0)
    },
    {
      title: 'Height (inches)',
      dataIndex: 'height',
      key: 'height',
      sorter: (a, b) => {
        const aHeightSplit = a.height.split('-').map(h => Number(h))
        const bHeightSplit = b.height.split('-').map(h => Number(h))

        if (aHeightSplit[0] === bHeightSplit[0]) {
          return aHeightSplit[1] - bHeightSplit[1];
        }

        return aHeightSplit[0] - bHeightSplit[0];
      }
    },
    {
      title: 'Weight (pounds)',
      dataIndex: 'weight',
      key: 'weight',
      filters: [
        { text: 'Toy (0-12)', value: '0-12' },
        { text: 'Small (13-22)', value: '13-22' },
        { text: 'Medium (23-57)', value: '23-57' },
        { text: 'Large (57-99)', value: '57-99' },
        { text: 'Giant (100+)', value: '100-99' }
      ],
      onFilter: (value, record) => {
        if (value) {
          const valueSplit = value.split('-')
          const valueArray = valueSplit.map(w => Number(w))
          const weightSplit = record.weight.split('-')
          const weightArray = weightSplit.map(w => Number(w))

          return (weightArray[0] >= valueArray[0] && weightArray[0] <= valueArray[1]) ||
                  (weightArray[1] >= valueArray[0] && weightArray[1] <= valueArray[1])
        }

        return false;
      },
      sorter: (a, b) => {
        const aWeightSplit = a.weight.split('-').map(w => Number(w))
        const bWeightSplit = b.weight.split('-').map(w => Number(w))

        if (aWeightSplit[0] === bWeightSplit[0]) {
          return aWeightSplit[1] - bWeightSplit[1];
        }

        return aWeightSplit[0] - bWeightSplit[0];
      }
    },
    {
      title: 'Life Expectancy',
      dataIndex: 'life_expectancy',
      key: 'life_expectancy',
      sorter: (a, b) => {
        const aLifeExpectancySplit = a.life_expectancy.split('-').map(l => Number(l))
        const bLifeExpectancySplit = b.life_expectancy.split('-').map(l => Number(l))

        if (aLifeExpectancySplit[0] === bLifeExpectancySplit[0]) {
          return aLifeExpectancySplit[1] - bLifeExpectancySplit[1];
        }

        return aLifeExpectancySplit[0] - bLifeExpectancySplit[0];
      }
    },
    {
      title: 'AKC Group',
      dataIndex: 'group',
      key: 'group',
      onFilter: (value, record) => record.name.indexOf(value) === 0,
      sorter: (a, b) => a.group.localeCompare(b.group)
    },
  ];

  const getTableData = () => breedData.map(breed => {
    let breed_pop = ''
    let breed_height = ''
    let breed_weight = ''
    let breed_life = ''
    let breed_group = ''
    
    if (breed && breed['attributes']) {
      breed_pop = breed['attributes']['breed_popularity'];
      breed_height = breed['attributes']['height'];
      breed_weight = breed['attributes']['weight'];
      breed_life = breed['attributes']['life_expectancy'];
      breed_group = breed['attributes']['group'];
    }

    return {
      key: breed['_id'],
      breed_name: breed['breed_name'],
      breed_popularity: breed_pop,
      height: getStringOrRange(breed_height),
      weight: getStringOrRange(breed_weight),
      life_expectancy: getStringOrRange(breed_life),
      group: breed_group,
    }
  });

  // const onClickBreed = id => () => { history.push(`/breed/${id}`) }

  return (
    <>
      <h1>Breed Data Page</h1>

      <Table 
        columns={tableColumns}
        dataSource={getTableData()}
        onRow={(record, rowIndex) => {
          return { onDoubleClick: _event => history.push(`/breeds/${record['key']}`) }
        }}
        pagination={{ pageSizeOptions: ['5', '10', '15'] }}
      />
    </>
  );
}

export const BreedsList = withRouter(BreedsListC)

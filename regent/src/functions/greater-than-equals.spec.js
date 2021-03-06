import greaterThanOrEquals from './greater-than-equals';

describe('greaterThanOrEquals', () => {
  it('greaterThanOrEquals should be a function', () => {
    expect(typeof greaterThanOrEquals).toEqual('function');
  });

  it('greaterThan should return true if the value given is greater than the param', () => {
    let actual = greaterThanOrEquals(1, 0);
    let expected = true;
    expect(actual).toEqual(expected);

    actual = greaterThanOrEquals(4, 3);
    expected = true;
    expect(actual).toEqual(expected);

    actual = greaterThanOrEquals(4.2, 4.1);
    expected = true;
    expect(actual).toEqual(expected);

    actual = greaterThanOrEquals(4, 4);
    expected = true;
    expect(actual).toEqual(expected);

    actual = greaterThanOrEquals(4.2, 4.2);
    expected = true;
    expect(actual).toEqual(expected);
  });

  it('greaterThan should return true if the value given is equal to the param', () => {
    let actual = greaterThanOrEquals(1, 1);
    let expected = true;
    expect(actual).toEqual(expected);

    actual = greaterThanOrEquals(4, 4);
    expected = true;
    expect(actual).toEqual(expected);

    actual = greaterThanOrEquals(4.2, 4.2);
    expected = true;
    expect(actual).toEqual(expected);
  });

  it('greaterThanOrEquals should return false if the value given is less than the param', () => {
    let actual = greaterThanOrEquals(1, 2);
    let expected = false;
    expect(actual).toEqual(expected);

    actual = greaterThanOrEquals(0, 10);
    expected = false;
    expect(actual).toEqual(expected);

    actual = greaterThanOrEquals(null, 4);
    expected = false;
    expect(actual).toEqual(expected);
  });

  it('greaterThanOrEquals should return false if the key is undefined', () => {
    const actual = greaterThanOrEquals(undefined, 0);
    const expected = false;
    expect(actual).toEqual(expected);
  });

  it('greaterThanOrEquals should return false if the key is a string that parses to NaN', () => {
    const redProps = [
      'cool',
      'some string',
      'undefined',
      'null',
      'false',
      'true',
    ];
    redProps.forEach((val) => {
      const actual = greaterThanOrEquals(val, 0);
      const expected = false;
      expect(actual).toEqual(expected);
    });
  });

  it('greaterThanOrEquals should compare strings based on standard lexicographical ordering, using Unicode values', () => {
    expect(greaterThanOrEquals('a', 'b')).toEqual(false);
    expect(greaterThanOrEquals('aaaa', 'abaa')).toEqual(false);
    expect(greaterThanOrEquals('bb', 'a')).toEqual(true);
    expect(greaterThanOrEquals('baa', 'abb')).toEqual(true);
    expect(greaterThanOrEquals('1', 2)).toEqual(false);
    expect(greaterThanOrEquals('2', 1)).toEqual(true);
    expect(greaterThanOrEquals('2', '4')).toEqual(false);
    expect(greaterThanOrEquals('2', '2')).toEqual(true);
    expect(greaterThanOrEquals(4, 4)).toEqual(true);
  });
});


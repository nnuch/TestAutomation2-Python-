import pytest 

############################# Fuzzy_math()
def fuzzy_math(num1, operator, num2):
    #Exception handle
    if type(num1) != int or type(num2) != int:
        raise Exception('We need to do fuzzy math on ints')

    #Cheak operator
    if operator == '+':
        result = num1 + num2
    elif operator == '*':
        result = num1 * num2
    else: 
        raise Exception(f"I don't know how to do math with '{operator}'")

    #Cheak result
    if result < 0: 
        return f'({result}:  A negative number, what does that even mean?'
    elif result < 10:
        return f'({result}:  A small number. I can deal with that'
    elif result < 20:
        return f'({result}:  A medium-sized number. OK.'
    else: 
        return f'({result}:  A really large number, way to big for me'


############################# Create the tests
class TestFuzzyMath:
    #Invalid input tests
    def test_non_int_input_for_num1(self):
        with pytest.raises(Exception) as exc_info:
            fuzzy_math('hi', '+', 2)
        assert 'fuzzy math on ints' in str(exc_info)
    
    def test_non_int_input_for_num2(self):
        with pytest.raises(Exception) as exc_info:
            fuzzy_math(2, '+','hi')
        assert 'fuzzy math on ints' in str(exc_info)

    #Addition tests 
    def test_addition_with_negative_result(self):
        assert 'negative number' in fuzzy_math(-5,'+',2)
        
    
    def test_addition_with_small_result(self):
        assert 'small number' in fuzzy_math(2,'+',2)

    def test_addition_with_medium_result(self):
        assert 'medium-sized number' in fuzzy_math(10,'+',2)
    
    def test_addition_with_large_result(self):
        assert 'large number' in fuzzy_math(200,'+',2)

    #Multiplication tests
    def test_multiplication_with_negative_result(self):
        assert 'negative number' in fuzzy_math(-2,'*',2)
    
    def test_multiplication_with_small_result(self):
        assert 'small number' in fuzzy_math(2,'*',2)

    def test_multiplication_with_medium_result(self):
        assert 'medium-sized number' in fuzzy_math(10,'*',1)
    
    def test_multiplication_with_large_result(self):
        assert 'large number' in fuzzy_math(200,'*',2)
    
    #Invalid operator test
    def test_invalid_operator(self):
        with pytest.raises(Exception) as exc_info:
            fuzzy_math(5, '-', 2)
        assert "don't know how to do math" in str(exc_info)
        
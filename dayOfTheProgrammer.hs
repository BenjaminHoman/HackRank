import Control.Applicative
import Control.Monad
import System.IO
import Data.List(inits)

divBy n i = n `mod` i == 0
divBy4 n = n `divBy` 4
isJulianLeap = divBy4
isGregorianLeap year = (year `divBy` 400) || ((divBy4 year) && not (year `divBy` 100))
    
getDOP year
    | year == 1918 = "26.09.1918"
    | year > 1918 = if isGregorianLeap year then leapDate else normalDate
    | year < 1918 = if isJulianLeap year then leapDate else normalDate
    where 
        combine prefix year = prefix ++ (show year)
        leapDate = "12.09." `combine` year
        normalDate = "13.09." `combine` year


main :: IO ()
main = do
    year_temp <- getLine
    let year = read year_temp :: Int
    putStrLn $ getDOP year

getMultipleLines :: Int -> IO [String]

getMultipleLines n
    | n <= 0 = return []
    | otherwise = do          
        x <- getLine         
        xs <- getMultipleLines (n-1)    
        let ret = (x:xs)    
        return ret  
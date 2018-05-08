% Pick a random city
% Pick a picture

% Pick a random picture from the same city

% Pair it with a city

Directory = 'correct_folder/';
cities = dir(Directory);
numCities = length(cities);

allPairs = cell(10, 2);
for i = 3:numCities
    city = cities(i).name;
%     savePath = strcat('resize256/', city);
%     mkdir(savePath);
    fullpath = strcat(Directory, city, '/');
    images = dir(fullpath);
    numImages = length(images);
    
    posPairs = [];
    for j = 3:numImages
        limit = 10;
        if (~isempty(posPairs))
           limit = limit - sum(posPairs(:, 2) == 20 * (i - 3) + (j - 2)); 
        end
        
        for z = 1:limit
            r = floor(17 .* rand(1,1) + 3);
            newRow = [20 * (i - 3) + (j - 2), 20 * (i - 3) + (r - 2)];
            if(j == r || (~isempty(posPairs) && sum(ismember(posPairs, newRow, 'rows')) ~= 0))
                limit = limit - 1; 
            else
                posPairs = [posPairs; newRow];
            end
        end
    end
    
    negPairs = [];
    for j = 3:numImages
        c = floor(3 .* rand(1,1) + 3);
        
        if(c == i)
            j = j - 1;
        else
            limit = 10;
            if (~isempty(negPairs))
               limit = limit - sum(negPairs(:, 2) == 20 * (i - 3) + (j - 2)); 
            end

            for z = 1:limit
                r = floor(17 .* rand(1,1) + 3);
                newRow = [20 * (i - 3) + (j - 2), 20 * (c - 3) + (r - 2)];
                if(j == r || (~isempty(negPairs) && sum(ismember(negPairs, newRow, 'rows')) ~= 0))
                    limit = limit - 1; 
                else
                    negPairs = [negPairs; newRow];
                end
            end
        end
    end
    
    allPairs{i - 2, 1} = posPairs;
    allPairs{i - 2, 2} = negPairs;
end

dlmwrite('pos.txt', posPairs, 'delimiter',' ');
dlmwrite('neg.txt', negPairs, 'delimiter',' ');

% Directory = 'resize256/';
% potato = allPairs{1, 2};
% p1 = potato(1, 1);
% a = imread(strcat(Directory, num2str(potato(1, 1)), '.png'));
% b = imread(strcat(Directory, num2str(potato(1, 2)), '.png'));
% 
% figure; imshow([a, b]);
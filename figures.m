% load data
% cd figs
mat = dir('*.mat'); 
for q = 1:length(mat) 
    load(mat(q).name); 
end

lineColor = [255, 155, 155; 
             255, 211, 155;
             250, 255, 155;
             155, 255, 168;
             155, 208, 255;
             202, 155, 255]./255;
lineColorProper = [251, 180, 174;
                   179, 205, 227;
                   204, 235, 197;
                   222, 203, 228;
                   254, 217, 166
                   ]./255;
colorDarker = [102,194,165;
               252,141,98;
               141,160,203;
               231,138,195;
               166,216,84
               ]./255;
           
% varying overlap degree
figure(1)
x = degrees;
for i = 1:size(varyDeg, 1)
    y = varyDeg(i,:);
    plot(x, y, 'Color', colorDarker(i,:), 'LineWidth', 1.5)
    hold all
end
%title('Reconstruction error with varying angle of overlap')
xlabel('Angle between consecutive views (\theta)')
xlim([3 18]);
ylim([0 4.5])
legend('x_{1}', 'x_{2}', 'y_{2}', 'z_{1}', 'z_{2}')
ylabel('Percentage error (%)')
xticks([3 6 9 12 15 18])
yticks([0 2 4])

%varying kernel size
figure(2)
set(subplot(1, 2, 1), 'Position', [.1 .35 .4 .4])
for i = 1:size(varyLPF, 1)
    x = kernelSizes;
    y = varyLPF(i,:);
    plot(x, y, 'Color', colorDarker(i,:), 'LineWidth', 1.5)
    hold all
end
ax = gca;
ax.XDir = 'reverse';
xlabel('Kernel size: \leftarrow Low Pass, High Pass \rightarrow')
xlim([0 9])
xticks([0 1 3 5 7 9])
ylabel('Percentage error (%)')
ylim([0 4.5])
yticks([0 2 4])

set(subplot(1, 2, 2),'Position',[.5 .35 .4 .4])
for i = 1:size(varyHPF, 1)
    x = kernelSizes;
    y = varyHPF(i, :);
    plot(x, y, 'Color', colorDarker(i,:), 'LineWidth', 1.5)
    hold all
end
xlim([0 9])
xticks([0 1 3 5 7 9])
ylim([0 4.5])
set(gca,'ytick',[])
legend('x_{1}', 'x_{2}', 'y_{2}', 'z_{1}', 'z_{2}')

%feature matching for conv. filters
figure(3)
set(subplot(1, 2, 1), 'Position', [.1 .35 .4 .4])
x = kernelSizes;
xlim([0 9])
xticks([0 1 3 5 7 9])
xlabel('Kernel size: \leftarrow Low Pass, High Pass \rightarrow')

y1 = matches(1, 1:size(kernelSizes, 2));
yyaxis left
plot(x, y1, 'Color', colorDarker(1,:), 'LineWidth', 1.5)
ylim([32 45])
yticks([32 38 44])
ylabel('% of features matched')
set(gca, 'ycolor', colorDarker(1,:), 'LineWidth', 1.5)

y2 = inliers(1, 1:size(kernelSizes, 2));
yyaxis right
plot(x, y2, 'Color', colorDarker(2, :), 'LineWidth', 1.5)
ylim([88 92])
set(gca,'ytick',[], 'ycolor', 'k')
ax = gca;
ax.XDir = 'reverse';

set(subplot(1, 2, 2),'Position',[.5 .35 .4 .4])
y1 = matches(2, 1:size(kernelSizes, 2));
yyaxis left
plot(x, y1, 'Color', colorDarker(1,:), 'LineWidth', 1.5)
ylim([32 45])
set(gca,'ytick',[], 'ycolor', 'k')


y2 = inliers(2, 1:size(kernelSizes, 2));
yyaxis right
plot(x, y2, 'Color', colorDarker(2, :), 'LineWidth', 1.5)
ylim([88 92])
yticks([88 90 92])
xlim([0 9])
xticks([0 1 3 5 7 9])
ylabel('% of match inliers')

% varying resolution
figure(4)
x = resPercentage;
for i = 1:size(varyRes, 1)
    y = varyRes(i,:);
    plot(x, y, 'Color', colorDarker(i,:), 'LineWidth', 1.5)
    hold all
end
%title('Reconstruction error with downsampling')
xlabel('% of original image resolution')
xlim([30 100]);
xticks([30 50 70 90 100])
yticks([0 2 4])
legend('x_{1}', 'x_{2}', 'y_{2}', 'z_{1}', 'z_{2}')
ylabel('Percentage error (%)')

%feature matching for res.
figure(5)
x = resPercentage;
y1 = matches(3, 1:size(resPercentage, 2));
yyaxis left
plot(x, y1, 'Color', colorDarker(1,:), 'LineWidth', 1.5)
ylim([35 40])
yticks([35 36 37 38 39 40])
ylabel('% of features matched')
set(gca, 'ycolor', colorDarker(1,:), 'LineWidth', 1.5)

y2 = inliers(3, 1:size(resPercentage, 2));
yyaxis right
plot(x, y2, 'Color', colorDarker(2, :), 'LineWidth', 1.5)
ylim([89 92])
yticks([89 90 91 92])
xlim([30 100])
xticks([30 50 70 90 100])
ylabel('% of match inliers')
xlabel('% of original image resolution')

% % varying clip limit
figure(6)
x = clipLimit;
for i = 1:size(varyClipLim, 1)
    y = varyClipLim(i,:);
    plot(x, y, 'Color', colorDarker(i,:), 'LineWidth', 1.5)
    hold all
end
%title('Reconstruction error with varying contrast')
xlabel('Clip limit')
ylabel('Percentage error (%)')
yticks([0 5 10])
legend('Inner distance')

%feature matching for contrast
figure(7)
x = clipLimit;
y1 = matches(4, 1:size(clipLimit, 2));
yyaxis left
plot(x, y1, 'Color', colorDarker(1,:), 'LineWidth', 1.5)
ylim([20 33])
yticks([22 26 32])
ylabel('% of features matched')
set(gca, 'ycolor', colorDarker(1,:), 'LineWidth', 1.5)

y2 = inliers(4, 1:size(clipLimit, 2));
yyaxis right
plot(x, y2, 'Color', colorDarker(2, :), 'LineWidth', 1.5)
ylim([90 93])
yticks([90 91 92 93])
xlim([0 3])
ylabel('% of match inliers')
xlabel('Clip limit')
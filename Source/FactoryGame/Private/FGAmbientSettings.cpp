// This file has been automatically generated by the Unreal Header Implementation tool

#include "FGAmbientSettings.h"

#if WITH_EDITOR
void UFGAmbientSettings::CheckForErrors(){ }
#endif 
UFGAmbientSettings::UFGAmbientSettings() : Super() {
	
}
UAkAudioEvent* UFGAmbientSettings::GetEnterOuterVolumeEvent_Implementation() const{ return nullptr; }
UAkAudioEvent* UFGAmbientSettings::GetEnterInnerVolumeEvent_Implementation() const{ return nullptr; }
void UFGAmbientSettings::OnEnterOuterVolume_Implementation( UAkComponent* ambientComponent) const{ }
void UFGAmbientSettings::OnExitOuterVolume_Implementation( UAkComponent* ambientComponent) const{ }
void UFGAmbientSettings::OnEnterInnerVolume_Implementation( UAkComponent* ambientComponent) const{ }
void UFGAmbientSettings::OnExitInnerVolume_Implementation( UAkComponent* ambientComponent) const{ }
bool UFGAmbientSettings::ShouldIgnoreListenerRotation_Implementation() const{ return bool(); }
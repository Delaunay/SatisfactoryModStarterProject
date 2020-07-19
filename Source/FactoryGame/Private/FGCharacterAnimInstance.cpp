// This file has been automatically generated by the Unreal Header Implementation tool

#include "FGCharacterAnimInstance.h"

UFGCharacterAnimInstance::UFGCharacterAnimInstance() : Super() {
	this->mAimYawInterpSpeed = 5;
	this->mYawRotationStrength = 7;
	this->mYawRotationInterpSpeed = 5;
	this->mRootRotationInterpSpeed = 5;
	this->mTurnInPlaceDefaultTime = 0.800000011920929;
	this->mYawAimMaxValue = 45;
	this->mYawAimMinValue = 45;
	this->mAimPitchInterpSpeed = 5;
	this->mPreLandVelocityMultiplier = 5;
	this->mPreLandCollisionChannels.Add(ECC_WorldStatic);
}
void UFGCharacterAnimInstance::NativeUpdateAnimation(float DeltaSeconds){ }
void UFGCharacterAnimInstance::OnPointDamageTaken_Implementation(FVector shootDIrection){ }
void UFGCharacterAnimInstance::OnAnyDamageTaken_Implementation(){ }
void UFGCharacterAnimInstance::OnRadialDamageTaken_Implementation(){ }
FRotator UFGCharacterAnimInstance::GetDesiredWalkRotation(){ return FRotator(); }
FRotator UFGCharacterAnimInstance::GetDesiredRunLeanRotation(){ return FRotator(); }
void UFGCharacterAnimInstance::TurnInPlaceEvent(float dt){ }
FVector UFGCharacterAnimInstance::GetCharacterVelocity()const{ return FVector(); }